#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

import click


def display_products(products):
    if products:
        line = "+-{}-+-{}-+-{}-+-{}-+".format("-" * 4, "-" * 30, "-" * 20, "-" * 10)
        print(line)
        print(
            "| {:^4} | {:^30} | {:^20} | {:^10} |".format(
                "№", "Название продукта", "Название магазина", "Стоимость"
            )
        )
        print(line)
        for idx, product in enumerate(products, 1):
            print(
                "| {:>4} | {:<30} | {:<20} | {:>10} |".format(
                    idx,
                    product.get("product_name", ""),
                    product.get("product_market", ""),
                    product.get("value", 0),
                )
            )
        print(line)

    else:
        print("Список продуктов пуст.")


def load_products(file_name):
    """
    Загрузить всех работников из файла JSON.
    """
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)


def save_products(file_name, staff):
    """
    Сохранить всех работников в JSON.
    """
    with open(file_name, "w", encoding="utf-8") as fount:
        json.dump(staff, fount, ensure_ascii=False, indent=4)


@click.group()
def commands():
    pass


@commands.command("add")
@click.argument("filename")
@click.option("--product_name", help="Name of product")
@click.option("--market_name", help="Name of market")
@click.option("--value", default=1, help="Value of product")
def add(filename, product_name, market_name, value):
    """
    Добавить данные о работнике.
    """
    products = load_products(filename)
    product = {
        "product_name": product_name,
        "product_market": market_name,
        "value": value,
    }
    products.append(product)
    save_products(filename, products)


@commands.command("display")
@click.argument("filename")
def display_product(filename):
    """
    Отобразить список работников.
    """
    products = load_products(filename)
    display_products(products)


@commands.command("select")
@click.argument("filename")
@click.argument("name")
def select(filename, name):
    """
    Выбрать продукт с заданным именем.
    """
    products = load_products(filename)
    result = []
    for product in products:
        if product.get("product_name") == name:
            result.append(product)

    display_products(result)


def main():
    commands()


if __name__ == "__main__":
    main()
